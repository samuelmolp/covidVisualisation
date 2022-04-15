document.addEventListener("DOMContentLoaded", function(){
    loadVideo("Daily cases by 100.000 people", "world");

    let filter = document.querySelector("#videoTypeSelect");
    filter.addEventListener("change", function(){
        let selectedOption = $("#videoTypeSelect").children("option:selected").val();
        let selectedRegion = $("#regionSelectVideo").children("option:selected").val();
        
        if (selectedRegion=="South America"){
            selectedRegion = "south_america";
        }
        loadVideo(selectedOption, selectedRegion);
    });

    document.querySelector("#videoSpeedInput").addEventListener("change", function(){
        let speed = $("#videoSpeedInput").children("option:selected").val();
        changeSpeed(speed);
    });

    document.querySelector("#regionSelectVideo").addEventListener("change", function(){
        let selectedRegion = $("#regionSelectVideo").children("option:selected").val();
        let selectedType = $("#videoTypeSelect").children("option:selected").val();
        if (selectedRegion=="South America"){
            selectedRegion = "south_america";
        }
        loadVideo(selectedType, selectedRegion);
    });
});


function loadVideo(type, region){
    let area = document.querySelector(".videos");

    $(area).empty();

    let video = document.createElement("video");
    video.className = "video_img";
    video.controls = true;

    if (type=="Daily cases by 100.000 people"){
        video.innerHTML = `<source src="/static/visualitation/Videos/relative_cases_${region.toLowerCase()}_video.mp4"  type="video/mp4">`;
    } else if (type=="Cases by 100.000 people in last 5 days"){
        video.innerHTML = `<source src="/static/visualitation/Videos/5days_relative_cases_${region.toLowerCase()}_video.mp4"  type="video/mp4">`;        
    } else if (type=="Daily cases"){
        video.innerHTML = `<source src="/static/visualitation/Videos/cases_${region.toLowerCase()}_video.mp4"  type="video/mp4">`;
    }

    area.appendChild(video);
}


function changeSpeed(speed){
    if (speed==="x0.5"){
        document.querySelector("video").playbackRate = 0.5;
    } else if (speed=="x1 (normal)"){
        document.querySelector("video").playbackRate = 1.0;
    } else if (speed==="x2"){
        document.querySelector("video").playbackRate = 2.0;
    } else if (speed==="x3"){
        document.querySelector("video").playbackRate = 3.0;
    } else if (speed==="x5"){
        document.querySelector("video").playbackRate = 5.0;
    }
}   