// Event listeners
const includeConsLogs = true;



function setTooltip(message) {
    $('#copy')
        .tooltip('hide')
        .attr('data-bs-original-title', message)
        .tooltip('show')
}

function hideTooltip(message) {
    setTimeout(function () {
        $('#copy')
            .tooltip('hide')
            .removeAttr('data-bs-original-title')
    }, 1500);
}

$(document).ready(function () {
    const icebreakerText = document.querySelector("#icebreaker")
    $("#copy").click(function(){
        navigator.clipboard.writeText(icebreakerText.textContent);
        if (includeConsLogs) {
            console.log(`icebreaker text copied:\n${icebreakerText.textContent}`);
        }
        setTooltip('Copied!');
        hideTooltip();
    });
});
