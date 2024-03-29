import matplotlib.pyplot as plt


def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend,
             legend_fontsize, title, title_fontsize, xlabel_fontsize,
             ylabel_fontsize):
    """设置matplotlib的轴"""
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend, loc='best', fontsize=legend_fontsize)
    if title:
        axes.set_title(title)
    axes.title.set_fontsize(title_fontsize)
    axes.xaxis.label.set_fontsize(xlabel_fontsize)
    axes.yaxis.label.set_fontsize(ylabel_fontsize)
    axes.grid()


def plot(X, Y=None,
         xlabel=None, ylabel=None,
         legend=None,
         xlim=None, ylim=None,
         xscale='linear', yscale='linear',
         figsize=None, axes=None, title=None,
         title_fontsize=26, xlabel_fontsize=20, ylabel_fontsize=20, legend_fontsize=14,
         # plot
         plot_fmts=('-', 'm--', 'g-.', 'r:'),
         # scatter
         scatter_fmts=('+', 'x', '*', '1'),
         # hist
         bins=30, density=False, hist_alpha=0.5, edgecolor='black',
         # mode
         mode='plot'):
    """绘制数据点"""
    if legend is None:
        legend = []
    if figsize:
        plt.rcParams['figure.figsize'] = figsize
    axes = axes if axes else plt.gca()

    # 如果X有一个轴，输出True
    def has_one_axis(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list)
                and not hasattr(X[0], "__len__"))

    if mode != 'hist':
        if has_one_axis(X):
            X = [X]
        if Y is None:
            X, Y = [[]] * len(X), X
        elif has_one_axis(Y):
            Y = [Y]
        if len(X) != len(Y):
            X = X * len(Y)
    axes.cla()
    if mode == 'scatter':
        for x, y, fmt in zip(X, Y, scatter_fmts):
            if len(x):
                axes.scatter(x, y, marker=fmt)
            else:
                axes.scatter(y, marker=fmt)
    elif mode == 'plot':
        for x, y, fmt in zip(X, Y, plot_fmts):
            if len(x):
                axes.plot(x, y, fmt)
            else:
                axes.plot(y, fmt)
    elif mode == 'hist':
        kwargs = dict(bins=bins, density=density, alpha=hist_alpha, edgecolor=edgecolor)
        for x in X:
            axes.hist(x, **kwargs)
    else:
        raise ValueError(f"Unknown mode: {mode}")
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend,
             legend_fontsize, title, title_fontsize, xlabel_fontsize,
             ylabel_fontsize)
    plt.show()
