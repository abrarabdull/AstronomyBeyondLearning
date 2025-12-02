document.addEventListener("DOMContentLoaded", () => {
    const svg = document.querySelector(".border-anim");
    if (!svg) return;

    const rects = svg.querySelectorAll("rect");

    const width = svg.clientWidth;
    const height = svg.clientHeight;
    const perimeter = 2 * (width + height);

    rects.forEach(rect => {
        rect.setAttribute("width", width);
        rect.setAttribute("height", height);
        rect.style.setProperty("--perimeter", perimeter);
        rect.style.strokeDasharray = perimeter;
        rect.style.strokeDashoffset = perimeter;
    });
});
