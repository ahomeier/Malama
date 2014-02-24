#import matplotlib.pyplot as plt
import pickle


def save_fig(fig, savename):
    fig_dikt = {'fig_info': get_figure_info(fig)}
    axes = fig.get_axes()
    for i, ax in enumerate(axes):
        ax_info = get_ax_info(ax)
        lines_info = get_lines_info(ax.lines)
        patches_info = get_patches_info(ax.patches)
        fig_dikt[('ax', i)] = {'ax_info': ax_info,
                               'lines': lines_info,
                               'patches': patches_info}
    pickle.dump(fig_dikt, open(savename, "wb"))


def get_figure_info(fig):
    return {'set_agg_filter': fig.get_agg_filter(),
            'set_alpha': fig.get_alpha(),
            'set_animated': fig.get_animated(),
            'set_dpi': fig.get_dpi(),
            'set_edgecolor': fig.get_edgecolor(),
            'set_facecolor': fig.get_facecolor(),
            'set_figheight': fig.get_figheight(),
            'set_figwidth': fig.get_figwidth(),
            'set_frameon': fig.get_frameon(),
            'set_gid': fig.get_gid(),
            'set_label': fig.get_label(),
            'set_size_inches': fig.get_size_inches(),
            'set_tight_layout': fig.get_tight_layout(),
            'set_visible': fig.get_visible(),
            'set_zorder': fig.get_zorder()}


def get_lines_info(lines):
    dikt = {}
    for line in lines:
        if '_line' in line.get_label():
            raise Exception('Please specify a label for each plot!')
        dikt[line.get_label()] = \
            {'set_aa': line.get_aa(),
             'set_agg_filter': line.get_agg_filter(),
             'set_alpha': line.get_alpha(),
             'set_animated': line.get_animated(),
             'set_antialiased': line.get_antialiased(),
             'set_c': line.get_c(),
             'set_clip_on': line.get_clip_on(),
             'set_clip_path': line.get_clip_path(),
             'set_dash_capstyle': line.get_dash_capstyle(),
             'set_dash_joinstyle': line.get_dash_joinstyle(),
             'set_data': line.get_data(),
             'set_drawstyle': line.get_drawstyle(),
             'set_fillstyle': line.get_fillstyle(),
             'set_label': line.get_label(),
             'set_linestyle': line.get_linestyle(),
             'set_linewidth': line.get_linewidth(),
             'set_marker': line.get_marker(),
             'set_markeredgecolor': line.get_markeredgecolor(),
             'set_markeredgewidth': line.get_markeredgewidth(),
             'set_markerfacecolor': line.get_markerfacecolor(),
             'set_markerfacecoloralt': line.get_markerfacecoloralt(),
             'set_markersize': line.get_markersize(),
             'set_markevery': line.get_markevery(),
             'set_mec': line.get_mec(),
             'set_mew': line.get_mew(),
             'set_mfc': line.get_mfc(),
             'set_mfcalt': line.get_mfcalt(),
             'set_ms': line.get_ms(),
             #'set_path': line.get_path(),
             'set_path_effects': line.get_path_effects(),
             'set_picker': line.get_picker(),
             'set_pickradius': line.get_pickradius(),
             'set_rasterized': line.get_rasterized(),
             'set_sketch_params': line.get_sketch_params(),
             'set_snap': line.get_snap(),
             'set_solid_capstyle': line.get_solid_capstyle(),
             'set_solid_joinstyle': line.get_solid_joinstyle(),
             #'set_get_transformed_clip_path_and_affine':
             #line.get_transformed_clip_path_and_affine(),
             'set_url': line.get_url(),
             'set_visible': line.get_visible(),
             'set_xdata': line.get_xdata(),
             #'set_xydata': line.get_xydata(),
             'set_ydata': line.get_ydata(),
             'set_zorder': line.get_zorder()}
    return dikt


def get_patches_info(patches):
    dikt = {}
    if patches and patches[0].get_label() == '_nolegend_':
        raise Exception('First histogram has no label!')
    for patch in patches:
        if patch.get_label() != '_nolegend_':
            label = patch.get_label()
            dikt[label] = []
        dikt[label].append({'set_aa': patch.get_aa(),
                            'set_agg_filter': patch.get_agg_filter(),
                            'set_alpha': patch.get_alpha(),
                            'set_animated': patch.get_animated(),
                            'set_antialiased': patch.get_antialiased(),
                            'set_clip_on': patch.get_clip_on(),
                            'set_clip_path': patch.get_clip_path(),
                            'set_contains': patch.get_contains(),
                            'set_ec': patch.get_ec(),
                            'set_edgecolor': patch.get_edgecolor(),
                            'set_facecolor': patch.get_facecolor(),
                            'set_fc': patch.get_fc(),
                            'set_fill': patch.get_fill(),
                            'set_gid': patch.get_gid(),
                            'set_hatch': patch.get_hatch(),
                            'set_height': patch.get_height(),
                            'set_label': patch.get_label(),
                            'set_linestyle': patch.get_linestyle(),
                            'set_linewidth': patch.get_linewidth(),
                            'set_ls': patch.get_ls(),
                            'set_lw': patch.get_lw(),
                            #'set_verts': patch.get_verts(),
                            'set_visible': patch.get_visible(),
                            'set_width': patch.get_width(),
                            'set_x': patch.get_x(),
                            'set_xy': patch.get_xy(),
                            'set_y': patch.get_y(),
                            'set_zorder': patch.get_zorder()})
    print 'You saved %i histograms!' % len(dikt)
    return dikt


def get_ax_info(ax):
    return {'set_yscale': ax.get_yscale(),
            'set_xscale': ax.get_xscale(),
            'set_xlim': ax.get_xlim(),
            'set_ylim': ax.get_ylim(),
            'set_xticks': ax.get_xticks(),
            'set_yticks': ax.get_yticks(),
            'set_xlabel': ax.get_xlabel(),
            'set_ylabel': ax.get_ylabel(),
            'set_title': ax.get_title(),
            #'x_gridlines': ,
            #'y_gridlines': ,
            #FIXME: implement grid information
            #FIXME: colorbar
            'rowNum': ax.rowNum,
            'numRows': ax.numRows,
            'colNum': ax.colNum,
            'numCols': ax.numCols}
