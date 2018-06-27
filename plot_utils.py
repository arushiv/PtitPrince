import matplotlib.pyplot as plt
import seaborn as sns
import half_viol

def make_raincloud(x=None, y=None, hue=None, data=None, order=None, hue_order=None,
                   bw=.2, cut=0, scale="area", scale_hue=True, gridsize=100,
                   width=.8, inner=None, split=False, dodge=True, orient="y",
                   linewidth=None, color=None, palette=None, saturation=.75,
                   ax=None, figsize=(6,6), lablecounts=False, **kwargs):
    """
    Draw full raincloud using half_viol. 
    labelcounts = True counts the number of items in each group and add it to x axis labels
    ! This adds a column to your dataframe
    >>> hv.make_raincloud(data=tips, x="day", y="total_bill", lablecounts=True)
    """

    if lablecounts:
        newx = f"{x} (Counts)"
        data.loc[:,newx] = data[x].astype(str) + "\n(N = " + data.groupby([x])[x].transform('count').astype(str) + ")"
        x = newx

    """Make complete raincloud plot """

    f, ax = plt.subplots(figsize=figsize)
    # Draw a violinplot with a narrower bandwidth than the default
    ax = half_viol.half_violinplot(x, y, hue, data, order, hue_order,
                           bw, cut, scale, scale_hue, gridsize,
                           width, inner, split, dodge, orient, linewidth,
                           color, palette, saturation)
    ax = sns.stripplot(data=data, palette=palette, edgecolor="white", size=2, orient=orient,
                     x=x, y=y, jitter=1, zorder=0)
    ax = sns.boxplot(data=data, color="black", orient=orient, width=.15, x=x, y=y, zorder=10,
                   showcaps=True, boxprops={'facecolor':'none', "zorder":10},
                   showfliers=True, whiskerprops={'linewidth':2, "zorder":10}, saturation=1)
        
    return ax
                                                                
