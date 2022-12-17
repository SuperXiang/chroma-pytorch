from setuptools import setup, find_packages

setup(
  name = 'chroma-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Chroma - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/chroma-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'denoising diffusion',
    'protein design'
  ],
  install_requires=[
    'einops>=0.6',
    'invariant-point-attention',
    'torch>=1.6',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
