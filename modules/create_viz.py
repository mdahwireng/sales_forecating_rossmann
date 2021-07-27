import matplotlib.pyplot as plt
import seaborn as sns

def plot_purchase_behv(bf_df, dur_df, aft_df, title, save_path):
    bf_df = bf_df.copy()
    dur_df = dur_df.copy()
    aft_df = aft_df.copy()
    
    fig, ax = plt.subplots(figsize=(20,10))
    sns.set_style('darkgrid', {'axes.facecolor': '.9'})
    sns.set_palette(palette='deep')

    sns.lineplot(x='Day', y='Sales', label='5days before', data=bf_df.groupby(['DayOfWeek','Day']).sum(), ax=ax, color = 'blue')
    sns.lineplot(x='Day', y='Sales', label='Public Holiday', data=dur_df.groupby(['DayOfWeek','Day']).sum(), ax=ax, color = 'green')
    sns.lineplot(x='Day', y='Sales', label='5days after', data=aft_df.groupby(['DayOfWeek','Day']).sum(), ax=ax, color = 'red')

    ax.legend(loc='best', fontsize=16)
    ax.set_xlabel('Day',fontsize=16)
    ax.set_ylabel('Sales',fontsize=16)
    ax.tick_params(axis='x', rotation=45, labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    ax.set_title(title, fontsize=20)
    img_path ='img/'
    path = img_path + save_path
    fig.savefig(path)