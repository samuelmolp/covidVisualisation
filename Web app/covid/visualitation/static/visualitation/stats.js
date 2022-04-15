document.addEventListener("DOMContentLoaded", function(){
    getData("new");
    document.querySelector("#filtersForm").addEventListener("submit", function(e){
        e.preventDefault();
        getData("update");
    });
});

function getData(loadingType){
    let start_date = $("#start_date").val();
    let end_date = $("#end_date").val();
    let type = $("#typeSelect").val();
    let region = $("#regionSelect").val();

    fetch(`/getData/${start_date}/${end_date}/${type}/${region}`)
    .then (response => response.json())
    .then(data => {
        if (loadingType=="new"){
            loadGraphic(data);
        } else if(loadingType=="update"){
            updateGraphic(data);
        }
    });
}

function loadGraphic(rawData){
    let labels = Object.keys(rawData["data"]);
    let values = Object.values(rawData["data"]);
    const ctx = document.getElementById('myChart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            responsive:true,
            datasets: [{
                label: `${$("#typeSelect").val()} in ${$("#regionSelect").val()}`,
                data: values,
                backgroundColor: [
                    'grey',
                ],
                borderColor: [
                    'black'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}


function updateGraphic(rawData){
    myChart.data.datasets = [{
        label: `${$("#typeSelect").val()} in ${$("#regionSelect").val()}`,
        data: Object.values(rawData["data"]),
        backgroundColor: [
            'grey',
        ],
        borderColor: [
            'black'
        ],
        borderWidth: 1
    }]

    myChart.data.labels = Object.keys(rawData["data"]);
        
    myChart.update();
}