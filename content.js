function() replaceImage{
    console.log("The extension is working!")
    
    var imgs = document.getElementsByTagName("img");
    var imgSrcs = [];
    console.log(chrome.runtime.getURL("sexybeast.JPG"));    
    for (var i = 0; i < imgs.length; i++) {
        imgs[i].src = chrome.runtime.getURL("sexybeast.JPG");
    }
};

setInterval(replaceImage, 100);
