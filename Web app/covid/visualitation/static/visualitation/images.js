document.addEventListener("DOMContentLoaded", function(){

    loadImages("Daily cases by 100.000 people", "2021-01-01", "world");

    document.querySelector(".dateFilterform").addEventListener("submit", function(e){
        e.preventDefault();
        let selectedOption = $("#imageTypeSelect").children("option:selected").val();
        let date = $("#dateFilter").val();
        let region = $("#regionSelectIMage").val();
        if (region=="South America"){
            region = "south_america";
        }
        if (new Date(date) < new Date("2020-01-23") || new Date(date) > new Date("2022-03-04")){
            alert("Date must be between 2020-01-23 and 2022-03-04");
        } else {
            if (selectedOption=="Cases by 100.000 people in last 5 days" && new Date(date) < new Date("2020-01-27")){
                $(".video_images").empty();
                alert("For this type date must be between 2020-01-27 and 2022-03-04");
            } else {
                loadImages(selectedOption, date, region);
            }
        }
    }); 
});


function loadImages(type, date, region){
    $(".images").empty();

    let image = document.createElement("img");
    image.className = "video_img";

    if (type=="Daily cases by 100.000 people"){
        image.src = `/static/visualitation/Images/${region.toLowerCase()}/relative_daily_cases/${date}.png`;
        image.srcset = `/static/visualitation/Images/${region.toLowerCase()}/relative_daily_cases/${date}.png`;
    } else if (type=="Cases by 100.000 people in last 5 days"){
        image.src = `/static/visualitation/Images/${region.toLowerCase()}/5days_relative_cases/${date}.png`;
        image.srcset = `/static/visualitation/Images/${region.toLowerCase()}/5days_relative_cases/${date}.png`;
    } else if (type=="Daily cases"){
        image.src = `/static/visualitation/Images/${region.toLowerCase()}/daily_cases/${date}.png`;
        image.srcset = `/static/visualitation/Images/${region.toLowerCase()}/daily_cases/${date}.png`;
    }

    document.querySelector(".images").append(image);
}
