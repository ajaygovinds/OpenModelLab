def save_html(results, filename):

    rows = ""

    for item in results:

        rows += f"""
        <tr>
            <td>{item['model']}</td>
            <td>{item['parameters']}</td>
            <td>{item['layers']}</td>
            <td>{item['hidden_size']}</td>
            <td>{item['latency_ms']}</td>
            <td>{item['throughput']}</td>
        </tr>
        """

    html = f"""
    <html>
    <head>
        <title>OpenModelLab Comparison</title>
    </head>

    <body>

    <h1>OpenModelLab Model Comparison</h1>

    <table border="1">

    <tr>
        <th>Model</th>
        <th>Parameters</th>
        <th>Layers</th>
        <th>Hidden Size</th>
        <th>Latency(ms)</th>
        <th>Throughput</th>
    </tr>

    {rows}

    </table>

    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(html)

    return filename
