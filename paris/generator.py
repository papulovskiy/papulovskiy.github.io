#!/opt/local/bin/python3.5
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def get_points():
    return [
        (55.557913, 58.583721),
        (55.152727, 27.382438),
        (53.296639, 60.10156),
        (43.1951655, -80.4202045),
        (63.8164269, -139.2273615),
        (48.8588377, 2.2775171),
        (1.9261091, -157.5241887),
        (41.5046767, -85.8421812),
        (39.8556132, -84.8001283),
        (40.1084635, -78.647438),
        (35.2868624, -93.7534646),
        (42.2273692, -111.4207571),
        (39.61499, -87.720813),
        (38.2015913, -84.304727),
        (44.2438052, -70.5605536),
        (43.7277966, -82.889339),
        (39.4792177, -92.0153342),
        (43.0006253, -75.3159662),
        (40.797558, -81.1735792),
        (40.4036795, -80.5147573),
        (36.2975609, -88.351115),
        (33.6750957, -95.601732),
        (39.0055706, -77.9568953),
        (42.8579582, -91.3517834),
        (42.5810101, -88.19346),
        (43.7277966, -82.889339),
        (44.2207477, -70.5495665),
        (40.1245012, -83.9681383),
        (44.3239362, -70.5998894),
        (43.0797856, -96.7977637),
    ]


if __name__ == "__main__":

    fig = plt.figure(figsize=(40, 22.5))
    plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.00)

    m = Basemap(projection='robin', lon_0=0, resolution='c')
    # continents = m.fillcontinents(color='lightgray', lake_color='white')
    continents = m.fillcontinents(color='lightgray', lake_color='lightgray')

    for i, continent in enumerate(continents):
        continent.set_gid('continent')

    ax = fig.gca()
    for point in get_points():
        x, y = m(point[1], point[0])
        circle1 = plt.Circle((x, y), 100000, fill='red', alpha=0.7)
        circle1.set_gid("marker")
        art = ax.add_artist(circle1)

    plt.savefig('world.svg')
    # plt.savefig('world.png',dpi=75) # PNG output
