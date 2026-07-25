<html>
<head>
    <title>Brevet Times</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table { border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px 12px; }
        th { background: #f0f0f0; }
        button { margin: 5px; padding: 8px 16px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Brevet Control Times</h1>

    <form method="GET">
        <button type="submit" name="endpoint" value="listAll">All Times</button>
        <button type="submit" name="endpoint" value="listOpenOnly">Open Only</button>
        <button type="submit" name="endpoint" value="listCloseOnly">Close Only</button>
        <br><br>
        Top: <input name="top" type="number" placeholder="e.g. 3" style="width:60px" value="<?php echo isset($_GET['top']) ? $_GET['top'] : ''; ?>">
    </form>

    <?php
    if (isset($_GET['endpoint'])) {
        $endpoint = $_GET['endpoint'];
        $top = isset($_GET['top']) && $_GET['top'] != '' ? '?top=' . $_GET['top'] : '';
        $url = 'http://laptop-service/' . $endpoint . '/json' . $top;

        $json = file_get_contents($url);
        if ($json === false) {
            echo "<p>Error: could not reach API.</p>";
        } else {
            $data = json_decode($json, true);
            if (count($data) === 0) {
                echo "<p>No data found.</p>";
            } else {
                echo "<table><tr>";
                foreach (array_keys($data[0]) as $key) {
                    echo "<th>$key</th>";
                }
                echo "</tr>";
                foreach ($data as $row) {
                    echo "<tr>";
                    foreach ($row as $val) {
                        echo "<td>$val</td>";
                    }
                    echo "</tr>";
                }
                echo "</table>";
            }
        }
    }
    ?>
</body>
</html>