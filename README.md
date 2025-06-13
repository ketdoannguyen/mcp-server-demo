# MCP Server Demo

**MCP Server Demo** là một dự án mẫu nhằm mục đích hướng dẫn cách triển khai một server MCP (Model Context Protocol) sử dụng Docker. Repo này minh họa rõ ràng quy trình xây dựng và deploy MCP server lên môi trường container hóa, giúp dễ dàng quản lý, mở rộng và tích hợp.

## Tính năng

* Triển khai server theo chuẩn MCP.
* Hỗ trợ FastMCP và Server-Sent Events (SSE).
* Dễ dàng cấu hình và deploy bằng Docker.
* Sẵn sàng mở rộng và tích hợp các công cụ, resource mới.

## Yêu cầu hệ thống

* Docker
* Python 3.12+ (nếu chạy trực tiếp)

## Hướng dẫn deploy bằng Docker

### 1. Build Docker image

```bash
docker build -t mcp_server_demo .
```

### 2. Chạy container

**Mặc định server sẽ lắng nghe trên cổng 8000:**

```bash
docker run -it -p 8000:8000 mcp_server_demo
```

**Chạy với cổng tùy chỉnh:**

Ví dụ, muốn truy cập server qua cổng 8001 trên máy tính:

```bash
docker run -it -p 8001:8000 mcp_server_demo
```

Nếu muốn server bên trong container sử dụng cổng khác (vd: 8002):

```bash
docker run -it -p 8002:8002 -e PORT=8002 mcp_server_demo
```

## Hướng dẫn chạy trực tiếp bằng Python (đối với Linux)

**a. Cài đặt uv:**

```bash
# Dùng curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Dùng pip
pip install uv
```

**b. Cài đặt dependencies:**

```bash
# Tạo môi trường .venv python ảo
python -m venv .venv

# Kích hoạt môi trường
source .venv/bin/activate

# Cài đặt dependencies
uv sync --all-packages
```

**c. Chạy server:**

```bash
python src/mcp_test/server.py
```

Server mặc định chạy trên [http://localhost:8000/](http://localhost:8000/)

Có thể tùy chỉnh host/port bằng biến môi trường `HOST` và `PORT`:

```bash
export HOST=0.0.0.0
export PORT=8000
python src/mcp_test/server.py
```

## Cấu hình bằng biến môi trường

* `HOST`: Địa chỉ host (mặc định: `0.0.0.0`)
* `PORT`: Cổng server (mặc định: `8000`)
* `ENVIRONMENT`: Chế độ môi trường (`production` hoặc `development`)

## Tác giả

* ketdoannguyen – [ketdoannguyen.ai@gmail.com](mailto:ketdoannguyen.ai@gmail.com)
