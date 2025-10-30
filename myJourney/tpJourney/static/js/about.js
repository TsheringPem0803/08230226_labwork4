document.addEventListener("DOMContentLoaded", function() {
    console.log("About Me page loaded!");

    const img = document.querySelector(".profile-img");
    if(img){
        img.addEventListener("click", () => {
            alert("👋 Hello! This is Tshering Pelden.");
        });
    }
});
