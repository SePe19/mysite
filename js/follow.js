async function follow(followee_element) {
    followee_id = followee_element.value
    const formData = new FormData()
    formData.append('followee_id', followee_id)
    const response = await fetch("/follow", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const followButtons = document.getElementsByClassName("follow")
    for (let i = 0; i < followButtons.length; i++) {
        if (followButtons[i].value == followee_id) {
            followButtons[i].textContent = "Following"
            followButtons[i].onclick = function() {
                unfollow(this)
            }
        }
    }
    const followerCountElement = document.getElementById("followerCount")
    const followerCount = await getFollowerCount()
    followerCountElement.textContent = followerCount
    
    const followingCountElement = document.getElementById("followingCount")
    const followingCount = await getFollowingCount()
    followingCountElement.textContent = followingCount
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
    const followButtons = document.getElementsByClassName("follow")
    for (let i = 0; i < followButtons.length; i++) {
        if (followButtons[i].value == followee_id) {
            followButtons[i].textContent = "Follow"
            followButtons[i].onclick = function() {
                follow(this)
            }
        }
    }

    const followerCountElement = document.getElementById("followerCount")
    const followerCount = await getFollowerCount() // Fetch updated follower count for the specified user
    followerCountElement.textContent = followerCount

    const followingCountElement = document.getElementById("followingCount")
    const followingCount = await getFollowingCount() // Fetch updated following count for the specified user
    followingCountElement.textContent = followingCount
}

async function getFollowerCount() {
    try {
        const url = window.location.href;
        const parts = url.split("/");
        const username = parts[parts.length - 1];

        const response = await fetch(`/${username}/followers`);
        const clonedResponse = response.clone();

        const data = await clonedResponse.json();

        console.log(data.followers)
        if (clonedResponse.ok) {
            console.log(data.followers)
            console.log(parseTwitterNumber(data.followers))
            return parseTwitterNumber(data.followers);
        } else {
            throw new Error("Error fetching follower count: Invalid response");
        }
    } catch (error) {
        console.error("Error fetching follower count:", error);
        return 0;
    }
}

async function getFollowingCount() {
    try {
        const url = window.location.href;
        const parts = url.split("/");
        const username = parts[parts.length - 1];

        const response = await fetch(`/${username}/following`);
        const clonedResponse = response.clone();

        const data = await clonedResponse.json();

        if (clonedResponse.ok) {
            console.log(data.following)
            console.log(parseTwitterNumber(data.following))
            return parseTwitterNumber(data.following);
        } else {
            throw new Error("Error fetching following count: Invalid response");
        }
    } catch (error) {
        console.error("Error fetching following count:", error);
        return 0;
    }
}