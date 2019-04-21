// s.z
// customized from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

let graph_now;
const CAL_URL = '../calculate';
let graph_url = './contents/graph_example.json';
let sampler = 'exact';
let algorithm = 'min_vertex_cover';

function get_algorithm(){
    algorithm = document.getElementById('algorithm').value;
}

function get_sample(){
    sampler = document.getElementById('sampler').value;
    sampler.replace('"', '');
}

let svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

let simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

// TODO read json user uploaded
d3.json(graph_url, function(error, g){
    if (error) throw error;
    graph_now = g;
});

d3.json(graph_url, function (error, graph) {
    if (error) throw error;

    var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
        .attr('id', function(d){
            return 'l' + d.source + d.target;
        });

    var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph.nodes)
        .enter().append("circle")
        .attr("r", 5)
        .attr('id', function(d){
            return "n" + d.id;
        })
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    node.append("title")
        .text(function (d) {
            return d.id;
        });

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

    function ticked() {
        link
            .attr("x1", function (d) {
                return d.source.x;
            })
            .attr("y1", function (d) {
                return d.source.y;
            })
            .attr("x2", function (d) {
                return d.target.x;
            })
            .attr("y2", function (d) {
                return d.target.y;
            });

        node
            .attr("cx", function (d) {
                return d.x;
            })
            .attr("cy", function (d) {
                return d.y;
            });
    }
});

function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

function show_result(result) {
    for (i=0; i<result.length; i++) {
        d3.select("#n" + result[i]).attr('class', 'selected');
    }
}

function clear_result() {
    d3.selectAll(".selected").attr('class', '');
}

function calculate() {
    clear_result();
    // send graph to server
    fetch(CAL_URL, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'algorithm' :algorithm,
            'sampler': sampler,
            'graph': graph_now
        })
    }).then(function (response) {
        return response.text();
    }).then(function(text){
        show_result(JSON.parse(text).result)
    });

}