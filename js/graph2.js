// 设置常数
var MARGIN_6 = { top: 40, right: 40, bottom: 40, left: 40 };
var WIDTH_6 = 800 - MARGIN_6.left - MARGIN_6.right;
var HEIGHT_6 = 400 - MARGIN_6.top - MARGIN_6.bottom;

var CENTRE_6 = 260;

var matrix = [
    [0, 1, 2],
    [1, 0, 3],
    [2, 3, 0]
];

// 创建SVG容器
var svg = d3.select("#chart");

// 创建布局
var chord = d3.chord()
    .padAngle(0.05)
    .sortSubgroups(d3.descending);

// 计算布局
var chords = chord(matrix);

// 创建弦图路径生成器
var ribbon = d3.ribbon();

// 绘制弦图
svg.append("g")
    .attr("transform", "translate(250, 250)")
    .selectAll("path")
    .data(chords)
    .enter().append("path")
    .attr("d", ribbon)
    .attr("fill", "steelblue")
    .attr("opacity", 0.7)
    .attr("stroke", "white")
    .attr("stroke-width", 0.5);