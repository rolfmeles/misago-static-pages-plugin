document.addEventListener("DOMContentLoaded", function () {
    
    const quill = new Quill("#editor", {
        theme: "snow"
    });
    
    const hidden = document.getElementById("id_content");
    
    quill.on("text-change", function () {
        hidden.value = quill.root.innerHTML;
    });
    
});
