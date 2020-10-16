var index=0 ;
show() ;
function show() {
    var i ;
    var slides=document.getElementsByClassName("slideshows");
    for (i=0;1<slides.length;i++){
        slides[i].style.display="none";
    }
    index=index+1;
    if (index>slides.length){
        index=1;
    }
    slides[index-1].style.display="block";
    setTimeout(show,1500);

}

