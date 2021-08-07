document.addEventListener("DOMContentLoaded", () => {
    setTimeout(setText, 5000);
    function setText() {
        let i_f = document.querySelectorAll('iframe');
        i_f.forEach(ele => {
            ele = ele.contentDocument;
            ele.dir = "rtl";
            let h = ele.head;
            let e = document.createElement('style');
            e.append(document.createTextNode("p { font-family: 'iran-sans'; font-size: 20px;}"));
            h.append(e)
        })
    }
});