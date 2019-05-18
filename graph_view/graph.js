const SERVER_URL = '../';
const CAL_URL = SERVER_URL + 'calculate';
const MODEL_LIST_URL = SERVER_URL + 'models';
const GRAPH_URL_BASE = './graphs/';
const GRAPH_LIST_URL = GRAPH_URL_BASE + '/list.json';
let sampler = 'exact';
let algorithm = 'min_vertex_cover';
let graph_name = 'barbell';
let graph_list;
let graph_now;

function get_algorithm(){
    algorithm = document.getElementById('algorithm').value;
}

function get_sample(){
    sampler = document.getElementById('sampler').value;
}

function get_graph(){
    graph_name = document.getElementById('graph').value;
    update_graph();
}

// get model list
d3.json(MODEL_LIST_URL, function (error, data) {
    model_list = data;
    select_tag = document.getElementById('algorithm');
    for(i=0; i<model_list.length; i++){
        let option_tag = document.createElement('option');
        option_tag.value = model_list[i];
        option_tag.text = model_list[i];
        select_tag.appendChild(option_tag);
    }
});

// get graph list
d3.json(GRAPH_LIST_URL, function(error, data){
    graph_list = data['graph_names'];
    select_tag = document.getElementById('graph');
    for(i=0; i<graph_list.length; i++){
        let option_tag = document.createElement('option');
        option_tag.value = graph_list[i];
        option_tag.text = graph_list[i];
        select_tag.appendChild(option_tag);
    }
});

function update_graph(){
    let graph_url = GRAPH_URL_BASE + graph_name + '.json';
    graph_svg = document.getElementById("graph_view");
    if(graph_svg !== null){
        graph_svg.innerHTML = "";
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
}

function show_alert(message){
    doc_ob = document.getElementById('alert');
    doc_ob.style.display = 'block';
    doc_ob.innerText = message;
}

function hide_alert() {
    doc_ob = document.getElementById('alert');
    doc_ob.style.display = 'none';
    doc_ob.innerText = '';
}

function show_result(res) {
    res_type = res['type'];
    if(res_type === 'node') {
        hide_alert();
        node_list = res['result'];
        for (i = 0; i < node_list.length; i++) {
            d3.select("#n" + node_list[i]).attr('class', 'selected');
        }
    } else if(res_type === 'alert'){
        message = res['result'];
        show_alert(message);
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
        show_result(JSON.parse(text));
    });

}

update_graph();
