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
    const followerCountElement = document.getElementById("followerCount");
    const followerCount = await getFollowerCount(); // Fetch updated follower count
    // followerCountElement.textContent = followerCount;
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

async function getFollowerCount() {
    try {
        const url = window.location.href
        const parts = url.split("/")
        const username = parts[parts.length - 1]

        const response = await fetch(`/${username}/followers`); // Replace with the endpoint that returns the follower count
        const data = await response.json();

        if (response.ok) {
            return data.count; // Assuming the response contains the count value
        } else {
            throw new Error("Error fetching follower count: Invalid response");
        }
    } catch (error) {
        console.error("Error fetching follower count:", error);
        return 0; // Return a default value or handle the error as needed
    }
}