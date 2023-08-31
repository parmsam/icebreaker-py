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

// Event listeners
$(document).ready(function () {
    const obsSlider = document.querySelector('#obs');
    let v = obsSlider.value;
    const icebreakerText = document.querySelector("#icebreaker")
    $("#copy").click(function(){
        navigator.clipboard.writeText(icebreakerText.textContent);
        if (includeConsLogs) {
            console.log(`icebreaker text copied:\n${icebreakerText.textContent}`);
        }
        setTooltip('Copied!');
        hideTooltip();
    });
    // define keyboard shortcuts
    $(document).keydown(function (key) {
        // check if key is 'c'
        if (key.which === 67) {
            // press copy button
            $("#copy").click();
        }
        // check if key is 'r'
        if (key.which === 82) {
            // press random button
            $("#random").click();
        }
        // check if key is 'd'
        if (key.which === 68) {
            // press difficult button
            $("#difficulty").click();
        }
    });
});
