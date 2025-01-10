# Masked blurring

Common blurring techniques on images, such as [**Box blur**](https://en.wikipedia.org/wiki/Box_blur) and [**Gaussian blur**](https://en.wikipedia.org/wiki/Gaussian_blur), have demonstrated to deliver sharp edges.

Repo contains a prototype application created to find out a better and smoothier way to blur areas on images, with a more natural look.

## Application and libraries

Application was written in **Python 3.11** and uses some libraries:

- [**OpenCV**](https://opencv.org)
- [**NumPy**](https://numpy.org)
- [**Matplotlib**](https://matplotlib.org)
- [**Pillow**](https://python-pillow.github.io)

## Jupyter notebook

A Jupyter notebook was used to better explain the approach that was used to find the proper solution for it, with hands-on steps comparing results.

## How to run

Run the Jupyter application container and access the application via browser.

```sh
$ docker build -t masked-blurring .
$ docker run -it --rm -p 8888:8888 masked-blurring
```

Terminal will show which endpoint should be used to open the application.

```
[I 2025-01-09 08:22:47.256 ServerApp] Jupyter Server 2.15.0 is running at:
token=3b0573d2fd8e33c074605813e9ea51dba0f1641a29eb8018
[I 2025-01-09 08:22:47.256 ServerApp]     http://127.0.0.1:8888/tree?token=3b0573d2fd8e33c074605813e9ea51dba0f1641a29eb8018
[I 2025-01-09 08:22:47.256 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
````

## License

[GNU AGPLv3](./LICENSE)