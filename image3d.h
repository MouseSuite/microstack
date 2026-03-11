// Copyright (C) 2026 The Regents of the University of California
// Created by David W. Shattuck, Ph.D.
// SPDX-License-Identifier: LGPL-2.1-only
// https://spdx.org/licenses/LGPL-2.1-only.html

#ifndef Image3D_H
#define Image3D_H

#include <vector>
#include <string>
#include <cinttypes>

class Image3D {
public:
  void initialize(const uint32_t w, const uint32_t h, const uint32_t n);
  bool readTiff(const std::string &ifname, uint32_t z);
  std::vector<uint16_t> data;  
  uint32_t nx = 0;
  uint32_t ny = 0;
  uint32_t nz = 0;  

  uint16_t &operator[](const size_t i) { return data[i]; }
  uint16_t  operator[](const size_t i) const { return data[i]; }
  size_t offset(const size_t x, const size_t y) const { return x+nx*y; }
  size_t offset(const size_t x, const size_t y, const size_t z) const { return x+nx*(y+ny*z); }
  uint16_t &operator()(const size_t x, const size_t y)       { return data[x+nx*y]; }
  uint16_t  operator()(const size_t x, const size_t y) const { return data[x+nx*y]; }
  uint16_t &operator()(const size_t x, const size_t y, const size_t z)       { return data[x+nx*(y+ny*z)]; }
  uint16_t  operator()(const size_t x, const size_t y, const size_t z) const { return data[x+nx*(y+ny*z)]; }
  const uint16_t *slice(const size_t z) const { return &data[nx*ny*z]; }
  uint16_t *slice(const size_t z) { return &data[nx*ny*z]; }
};

#endif
