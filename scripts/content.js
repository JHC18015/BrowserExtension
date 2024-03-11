alert("Jimmy has commenced the toe sucking!")

var imgs = document.getElementsByTagName("img");
var imgSrcs = [];
    
for (var i = 0; i < imgs.length; i++) {
    imgs[i].src = chrome.runtime.getURL("scripts/sexybeast.jpg");
}
