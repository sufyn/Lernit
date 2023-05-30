$(document).ready(function(){
    var API_KEY = "AIzaSyDWq1xVykBUxpBMEHhKpMb0wsr_zucamAY"
    var order='viewcount'
    var video = ''
    
    
    $("#form").submit(function(event){
        event.preventDefault()
        var search = $("#search").val()
        videoSearch(API_KEY,search,4)
    })
    
    function videoSearch(key,search,maxResults,_viewcount){
        

        $("#videos").empty()
        $.get("https://www.googleapis.com/youtube/v3/search?key="+key+"&type=video&part=snippet&maxResults="+maxResults  + "&q="+search,function(data){
        console.log(data)
    
        data.items.forEach(item => {
            video = `
            <iframe width="820" height="515"
            src="https://www.youtube.com/embed/${item.id.videoId}" frameborder="10" allowfullscreen></iframe>
            `
            $("#videos").append(video)
        })

        }
    )
    for (var i = 0; i < maxResults.items.length; i++) {
        var video = maxResults.items[i];
       if (video.status.embeddable == false ||video.status.privacyStatus == 'public'||video.status.uploadStatus == 'available') {
         continue; 
       }
    } 
   
}



})

var button = document.getElementById("Test")
button.onclick = post
function post(){
search = document.getElementById("search").value 
        // Store the response in a cookie or local storage
localStorage.setItem("search", search);
    // Redirect to the results page
window.location.href = "/gpt2";
        // Redirect to the results page or update the DOM with the response data
        // processResponse(response)
        
    
    }  