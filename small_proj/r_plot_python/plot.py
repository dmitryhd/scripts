def create_plot_labels(columns, tags):
    """ Write file, creating headers for plot. """
    with open(cfg.LABELS_FILENAME, 'w+') as labels_fd:
        tag_index = 0
        for tag in tags:
            data = columns[tag_index]
            num = len(data)
            mean = int(sum(data))/len(data) if len(data) > 0 else 0
            mean = int(mean)
            label = '"' + tag.name
            label += ' От. Средн:{}, Вакансий:{}'.format(mean, num) + '" '
            print(label, file=labels_fd, end='')
            tag_index += 1
            data = columns[tag_index]
            num = len(data)
            mean = int(sum(data))/len(data) if len(data) > 0 else 0
            mean = int(mean)
            label = '"' + tag.name
            label += ' До. Средн:{}, Вакансий:{}'.format(mean, num) + '" '
            print(label, file=labels_fd, end='')
            tag_index += 1

def get_csv_header_and_columns(proc_vacs, tags):
    """ Return header, columns of data. """
    header = ''
    columns = []
    for tag in tags:
        header += tag.title + '_min '
        columns.append([])
        header += tag.title + '_max '
        columns.append([])
    for pvac in proc_vacs:
        tag_index = 0
        for tag in tags:
            if pvac.tags[tag.name] and pvac.min_salary:
                columns[tag_index].append(pvac.min_salary)
            tag_index += 1
            if pvac.tags[tag.name] and pvac.max_salary:
                columns[tag_index].append(pvac.max_salary)
            tag_index += 1
    return header, columns

def plot(gather_time_sec, site):
    """ Create plot png. """
    gather_time_str = datetime.fromtimestamp(gather_time_sec).strftime(
        "%Y-%m-%d")

    with open(cfg.TITLE_FILENAME, 'w') as label_fd:
        print(cfg.LABEL.format(site, gather_time_str), file=label_fd)
    with open(cfg.PLOT_FILENAME_CONTAINER, 'w') as plot_fd:
        print('plots/plot_{}_{}.png'.format(
            site, gather_time_sec), file=plot_fd)
    import subprocess;
    output = subprocess.check_output('Rscript ./plot.R',
                                     stderr=subprocess.DEVNULL,
                                     shell=True);
def output_csv(pvacs, tags, csv_file_name=cfg.CSV_FILENAME):
    """ Generate csv file with vacancy name, minimum and maximum salary
        anb information about programming language.
    """
    header, columns = get_csv_header_and_columns(pvacs, tags)
    max_length = 0
    for column in columns:
        max_length = max(max_length, len(column))
    for column in columns:
        need_to_fill = max_length - len(column)
        column.extend(['NA']*need_to_fill)
    #save result
    csv_fd = open(csv_file_name, 'w')
    print(header, file=csv_fd)
    for i in range(max_length):
        out = ''
        for column in columns:
            out += str(column[i]) + ' '
        print(out, file=csv_fd)
