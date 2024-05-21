#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        body {
            background-image: url(./360_F_389935531_ITV2B8SO2Gl69zHi9i1ytn95KrWFfMOo.jpg);
        }
    </style>
</head>

<body>
    <div class="offcanvas offcanvas-start w-25" tabindex="-1" id="offcanvas" data-bs-keyboard="false"
        data-bs-backdrop="false">
        <div class="offcanvas-header">
            <h6 class="offcanvas-title d-none d-sm-block" id="offcanvas">Menu</h6>
            <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body px-0">
            <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-start" id="menu">
                <li class="dropdown">
                    <a href="#" class="nav-link dropdown-toggle  text-truncate" id="dropdown" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <i class="fs-5"></i><span class="ms-1 d-none d-sm-inline">TASK</span>
                    </a>
                    <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdown">
                        <li><a class="dropdown-item" href="#">CREATE NEW TASK</a></li>
                        <li><a class="dropdown-item" href="#">EXISTING TASK</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="nav-link dropdown-toggle  text-truncate" id="dropdown" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <i class="fs-5"></i><span class="ms-1 d-none d-sm-inline">INVENTORY</span>
                    </a>
                    <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdown">
                        <li><a class="dropdown-item" href="#">INVENTORY REQUEST</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="nav-link dropdown-toggle  text-truncate" id="dropdown" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <i class="fs-5"></i><span class="ms-1 d-none d-sm-inline">LEAVE</span>
                    </a>
                    <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdown">
                        <li><a class="dropdown-item" href="#">NEW REQUEST</a></li>
                        <li><a class="dropdown-item" href="#">EXISTING REQUEST</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="nav-link dropdown-toggle  text-truncate" id="dropdown" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <i class="fs-5"></i><span class="ms-1 d-none d-sm-inline">SALARY</span>
                    </a>
                    <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdown">
                        <li><a class="dropdown-item" href="#">VIEW SALARY</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
    <div class="container-fluid">
        <div class="row">
            <div class="col min-vh-100 py-3">
                <!-- toggler -->
                <button class="btn float-end" data-bs-toggle="offcanvas" data-bs-target="#offcanvas" role="button">
                    <i class="bi bi-arrow-right-square-fill fs-3" data-bs-toggle="offcanvas"
                        data-bs-target="#offcanvas"></i>
                </button>
                <img src="./download (1).png" class="img-thumbnail" alt="..." height="100PX" width="70PX">
            </div>
        </div>
    </div>
</body>

</html>""")