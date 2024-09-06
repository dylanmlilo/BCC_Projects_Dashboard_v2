from flask import abort
import pandas as pd
import json
import plotly
import plotly_express as px
import plotly.graph_objects as go
from models.projects import ContractType, projects_data_to_dict_list
from datetime import datetime


def today_date():
    """
    Get the current date and format it as a string
    in the format 'Day, DD Month YYYY'.

    Returns:
        str: The formatted current date string.
    """
    today_date = datetime.today()

    formatted_date = today_date.strftime('%a, %d %B %Y')

    return formatted_date


def plot_home_page_charts():
    """
    Generates and returns JSON representations of
    various plots for projects data

    Returns:
    graph1JSON (str): JSON representation of the physical progress plot.
    graph2JSON (str): JSON representation of the reservoir levels plot.
    """
    projects_data = projects_data_to_dict_list()
    df = pd.DataFrame(projects_data)

    df_filtered_fig1 = df[df['physical_progress_percentage'].notnull()]

    fig1 = px.bar(df_filtered_fig1, x='contract_number',
                  y='physical_progress_percentage',
                  color='project_manager',
                  title="Physical Progress of Works")

    fig1.update_layout(
      legend_title_text='Project Managers',
      title={
          'x': 0.5,
          'y': 0.93,
          'font': {
              'size': 25,
              'family': 'Arial'
          }
      },
      xaxis_title_text="Contract Number",
      yaxis_title_text="Physical Progress (%)",
      xaxis_title_font_size=17,
      yaxis_title_font_size=17,
      legend_title_font={'size': 16},
      margin=dict(r=50, l=50, t=80, b=50),
      paper_bgcolor='rgba(0, 0, 0, 0.1)'
      )

    df_filtered_fig2 = df[df['financial_progress_percentage'].notnull()]

    fig2 = px.bar(df_filtered_fig2, x='contract_number',
                  y='financial_progress_percentage',
                  color='contract_type', title="Financial Progress of Works")
    fig2.update_layout(
      legend_title_text='Contract Type',
      title={
          'x': 0.5,
          'y': 0.93,
          'font': {
              'size': 25,
              'family': 'Arial'
          }
      },
      xaxis_title_text="Contract Number",
      yaxis_title_text="Financial Progress (%)",
      xaxis_title_font_size=17,
      yaxis_title_font_size=17,
      legend_title_font={'size': 16},
      margin=dict(r=50, l=50, t=80, b=50),
      paper_bgcolor='rgba(47, 182, 182, 0.2)'
      )

    projects_by_year = (
      df.groupby("year")
      .size()
      .reset_index(name="number_of_projects")
      )

    fig3 = px.pie(projects_by_year, values='number_of_projects', names='year',
                  title='Distribution of Projects by Year')

    fig3.update_layout(
      title={
          'x': 0.5,
          'y': 0.95,
          'font': {
              'size': 25,
              'family': 'Arial'
          }
      },
      margin=dict(t=60, b=20),
      paper_bgcolor='rgba(0, 0, 0, 0.1)'
      )

    projects_by_status = (
      df.groupby('project_status')
      .size().reset_index(name='number_of_projects')
      )

    color_map = {
        'Completed': '#109618',
        'Stopped': '#FB0D0D',
        'In Progress': '#00A08B',
        'Retendered': 'orange',
        'Yet to start': 'rgb(255, 166, 71)'
    }

    fig4 = px.treemap(projects_by_status,
                      path=['project_status'],
                      values='number_of_projects',
                      color='project_status',
                      color_discrete_map=color_map,
                      title='Distribution of Projects by Status')

    fig4.update_layout(
      title={
          'x': 0.5,
          'y': 0.93,
          'font': {
              'size': 22.5,
              'family': 'Arial'
          }
      },
      margin=dict(r=5, l=5, t=60, b=60),
      paper_bgcolor='rgba(47, 182, 182, 0.2)'
      )

    projects_by_manager = df['project_manager'].value_counts().reset_index()
    projects_by_manager.columns = ['project_manager', 'number_of_projects']

    fig5 = px.sunburst(projects_by_manager, path=['project_manager'],
                       values='number_of_projects',
                       title='Distribution of Projects by Project Managers')

    fig5.update_layout(
      title={
          'x': 0.5,
          'y': 0.95,
          'font': {
              'size': 22,
              'family': 'Arial'
          }
      },
      margin=dict(t=60, b=20),
      paper_bgcolor='rgba(0, 0, 0, 0.1)'
      )

    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    return graph1JSON, graph2JSON, graph3JSON, graph4JSON, graph5JSON


def plot_servicing_page_charts():
    """
    Generates a list of JSON representations of bar charts
    displaying project progress with colors.

    Returns:
        list: A list of JSON strings representing the Plotly charts,
        one for each project.
    """

    servicing_data = ContractType.contract_type_data_dict(1)
    servicing_charts = []

    if not servicing_data:
        return servicing_charts

    bg_colors = ['rgba(0, 0, 0, 0.1)', 'rgba(47, 182, 182, 0.2)']
    color_index = 0

    for project_data in servicing_data:
        contract_name = project_data.get("contract_name")
        contractor = project_data.get("contractor")
        link = project_data.get("link")
        progress_data = {
          "Progress Type": [
            "Water", "Sewer", "Roads", "Storm Drainage",
            "Public Lighting", "Total Progress"
          ],
          "Progress Percentage": [
            project_data["water_progress"],
            project_data["sewer_progress"],
            project_data["roads_progress"],
            project_data["storm_drainage_progress"],
            project_data["public_lighting_progress"],
            project_data["physical_progress_percentage"]
          ]
        }

        color_list = ['royalblue', 'goldenrod', 'grey',
                      'green', 'orange', 'red']

        fig = px.bar(progress_data, x="Progress Type", y="Progress Percentage",
                     title=contract_name, color=progress_data["Progress Type"],
                     color_discrete_sequence=color_list)
        fig.update_layout(
          legend_title="Progress Type",
          bargap=0.6,
          title={
            'text': contract_name,
            'x': 0.5,
            'y': 0.9,
            'font': {
              'size': 20,
              'family': 'Arial'
            }
          },
          xaxis_title_text=(
            "Contractor - {} -- <a href='{}'>Link to Google Drive Folder</a>"
            .format(contractor, link)
          ),
          yaxis_title_text="Progress Percentage(%)",
          xaxis_title_font_size=17,
          yaxis_title_font_size=17,
          legend_title_font={'size': 16},
          paper_bgcolor=bg_colors[color_index]
        )

        color_index = (color_index + 1) % len(bg_colors)

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        servicing_charts.append(graphJSON)

    return servicing_charts
