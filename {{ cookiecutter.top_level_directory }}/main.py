import os
import plotly.graph_objs as go
import streamlit as st

from core.parser import MAX_GRID_WIDTH, load_grid, add_border
from core.search import GridSearchProblem, breadth_first_search

st.set_page_config(page_title="Breadth-first search app")
st.title("Grid map search")
st.write(
    "Breadth-first search (BFS) is always complete and finds the shortest path to the goal, " +
    "but it's also uninformed. " +
    "Compared to an informed heuristic search like A*, BFS can be a slower performer, but on " +
    "small maps it does fine.")
grid_file = os.path.join("data", "grid.txt")
grid = add_border(load_grid(filename=grid_file))
problem = GridSearchProblem()
st.sidebar.title("Parameters")
label_col11, label_col12 = st.sidebar.columns(2, gap="small")
label_col11.caption("Start")
col11, col12 = st.sidebar.columns(2, gap="small")
txt_start_x = col11.number_input("X:",
                                 format="%d",
                                 min_value=1,
                                 max_value=MAX_GRID_WIDTH,
                                 value=problem.start[0])
txt_start_y = col12.number_input("Y:",
                                 format="%d",
                                 min_value=1,
                                 max_value=len(grid),
                                 value=problem.start[1])
label_col21, label_col22 = st.sidebar.columns(2, gap="small")
label_col21.caption("Goal")
col21, col22 = st.sidebar.columns(2, gap="small")
txt_goal_x = col21.number_input("X:",
                                format="%d",
                                min_value=1,
                                max_value=MAX_GRID_WIDTH,
                                value=problem.goal[0])
txt_goal_y = col22.number_input("Y:",
                                format="%d",
                                min_value=1,
                                max_value=len(grid),
                                value=problem.goal[1])

new_start = int(txt_start_x), int(txt_start_y)
new_goal = int(txt_goal_x), int(txt_goal_y)
problem = GridSearchProblem(start=new_start, goal=new_goal)
soln = breadth_first_search(problem)
island = problem.getGridPoints()
xs = [x for x, _ in island]
ys = [y for _, y in island]
land = go.Scatter(
    name="Terrain",
    x=xs,
    y=ys,
    mode="markers",
    marker={
        "showscale": False,
        "color": "green",
        "size": 20,
        "line": {
            "width": 0
        }
    },
)
if soln is not None:
    xs = [x for x, _ in soln[::-1]]
    ys = [y for _, y in soln[::-1]]
    path = go.Scatter(
        name="Solution path",
        x=xs,
        y=ys,
        mode="markers",
        marker={
            "showscale": False,
            "color": "mediumslateblue",
            "size": 20,
            "line": {
                "width": 0
            },
        },
    )
else:
    path = go.Scatter(x=[], y=[])

start = go.Scatter(
    name="Start",
    x=[int(txt_start_x)],
    y=[int(txt_start_y)],
    text="S",
    textposition="middle center",
    mode="markers+text",
    marker={
        "showscale": False,
        "color": "blue",
        "size": 20,
        "line": {
            "width": 0
        }
    },
)
goal = go.Scatter(
    name="Goal",
    x=[int(txt_goal_x)],
    y=[int(txt_goal_y)],
    text="G",
    textposition="middle center",
    mode="markers+text",
    marker={
        "showscale": False,
        "color": "purple",
        "size": 20,
        "line": {
            "width": 0
        }
    },
)
fig = go.Figure(
    data=[land, path, start, goal],
    layout=go.Layout(
        hovermode="closest",
        xaxis={
            "showgrid": False,
            "zeroline": False,
            "showticklabels": False
        },
        yaxis={
            "showgrid": False,
            "zeroline": False,
            "autorange": "reversed",
            "showticklabels": False,
        },
    ),
)
st.plotly_chart(fig, use_container_width=True)

if soln is not None:
    st.write(f"Path: {soln}")
else:
    st.write("Path: No solution found. Outside map boundary.")
