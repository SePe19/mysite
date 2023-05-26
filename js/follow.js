async function follow(followee_element) {
    followee_id = followee_element.value
    const formData = new FormData()
    formData.append('followee_id', followee_id)
    const response = await fetch("/follow", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const followButtons = document.getElementsByClassName("follow");
    for (let i = 0; i < followButtons.length; i++) {
        if (followButtons[i].value == followee_id) {
            followButtons[i].textContent = "Following";
            followButtons[i].onclick = function() {
                unfollow(this);
            };
        }
    }
}

async function unfollow(followee_element) {
    followee_id = followee_element.value
    const formData = new FormData()
    formData.append('followee_id', followee_id)
    const response = await fetch("/unfollow", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const followButtons = document.getElementsByClassName("follow");
    for (let i = 0; i < followButtons.length; i++) {
        if (followButtons[i].value == followee_id) {
            followButtons[i].textContent = "Follow";
            followButtons[i].onclick = function() {
                follow(this);
            };
        }
    }
}