function parseTwitterDate(tdate, is_tweet) {
    const system_date = new Date(tdate*1000)
    const user_date = new Date()

    const diff = Math.floor((user_date - system_date) / 1000)
    if (diff <= 1 && is_tweet) {return "just now"}
    if (diff < 20 && is_tweet) {return diff + " seconds ago"}
    if (diff < 40 && is_tweet) {return "half a minute ago"}
    if (diff < 60 && is_tweet) {return "less than a minute ago"}
    if (diff <= 90 && is_tweet) {return "one minute ago"}
    if (diff <= 3540 && is_tweet) {return Math.round(diff / 60) + " minutes ago"}
    if (diff <= 5400 && is_tweet) {return "1 hour ago"}
    if (diff <= 86400 && is_tweet) {return Math.round(diff / 3600) + " hours ago"}
    if (diff <= 129600 && is_tweet) {return "1 day ago"}
    if (diff < 604800 && is_tweet) {return Math.round(diff / 86400) + " days ago"}
    if (diff <= 777600 && is_tweet) {return "1 week ago"}
    if (system_date.getFullYear()==user_date.getFullYear() && is_tweet) {
        return getMonthName(system_date.getMonth()) + " " + system_date.getDate()
    }
    return getMonthName(system_date.getMonth()) + " " + system_date.getDate() + ", " + system_date.getFullYear()
}

function getMonthName(monthIndex) {
    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return monthNames[monthIndex]
}    

// User user_created_at
function user_created_time() {
    if (document.getElementById("joined_at")) {
        const joinedAtElement = document.getElementById("joined_at")
        const userCreatedAt = joinedAtElement.textContent
        joinedAtElement.textContent = "Joined " + parseTwitterDate(userCreatedAt, false)
    }
}

// Tweet tweet_created_at
function tweet_created_time() {
    const elements = document.querySelectorAll(".tweet-time")
    elements.forEach(function(element) {
        const tweetCreatedAt = element.textContent
        element.textContent = parseTwitterDate(tweetCreatedAt, true)
    })
}

user_created_time()
tweet_created_time()