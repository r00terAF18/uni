document.addEventListener("DOMContentLoaded", () => {
    setTimeout(setText, 2500);
    function setText() {
        let i_f = document.querySelector('iframe').contentDocument;
        i_f.dir = "rtl";

        let h = i_f.head;

        let e = document.createElement('style');

        e.append(document.createTextNode("p { font-family: 'iran-sans'}"));

        h.append(e)
    }
});