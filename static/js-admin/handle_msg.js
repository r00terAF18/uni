function handle_msg(msg_title = "title for message", msg_type = "success", msg_content = "Sample Success Message") {
    let url = window.location.origin + "/warning/";
    let data = {
        "title": msg_title,
        "type": msg_type,
        "content": msg_content
    }
    let c = document.cookie.replace("csrftoken=", "");
    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': c
        },
        credentials: 'same-origin',
        body: JSON.stringify(data)
    })
}