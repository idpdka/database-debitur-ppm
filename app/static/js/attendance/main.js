// Get weather status
const appKey = "565c95ffb730cb7204630ad743cf3c27";
const city = "jakarta";
let searchLink = "https://api.openweathermap.org/data/2.5/weather?q=" + city + ",id&appid="+appKey;
httpRequestAsync(searchLink, theResponse);

function theResponse(response) {
    let jsonObject = JSON.parse(response);
}

function httpRequestAsync(url, callback)
{
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = () => {
        if (httpRequest.readyState == 4 && httpRequest.status == 200)
            callback(httpRequest.responseText);
    }
    httpRequest.open("GET", url, true); // true for asynchronous
    httpRequest.send();
}