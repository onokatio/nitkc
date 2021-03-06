ネットワーク入門 調べ学習
===

# 1. 調査・実験テーマ
DNS検閲への対策
# 2. 1に関するキーワード
DNS 検閲 ブロッキング
# 3. 調査・実験をするに至った背景・経緯
NTTがDNSブロッキングを開始したことが大きなニュースになったため、自衛方法を学ぼうと思いました。
# 4. 明らかになっていないこと
DNS検閲への対策方法
# 5. 何を明らかにしたのか
国内から海外DNSサーバーへ安全に接続する。
# 6. 手段
## DNS-over-HTTPS, DNS-over-TLS, DNS-crypt

これらは、名前解決を、暗号化されたレイヤーの上で実行したり、DNSの通信自体に暗号化を施したものです。CloudflareやFacebook、有志のDNSが対応しています。

Android、iOS、Windows、Linuxなど、OSを選ばずにクライアントが公開されているので、難しいことをせずにすぐ利用することができます。


## DNS-over-Proxy

従来のSOCKSプロキシを使用するDNS名前解決です。これは自力でサーバーを構築する必要がありますが、サーバー自体は普通のProxyサーバーで済むことができます。

SOCKS Proxyよりも強固な暗号化・秘匿化を求める場合には、ShadowSocksと呼ばれる技術があります。ShadowSocksは中国のグレートファイアウォールを回避するために作られたプロトコルで、JSONを使った軽量・高速な通信ができるとのことです。

## VPN

VPNは最も有名なブロッキング回避技術です。OpenVPNやIPsecなどがありますが、一番高性能なものはSoftEtherVPNです。通称VPN-over-HTTPSと呼ばれる、L2接続をHTTPS接続の上で使用できる（偽装できる）通信方式に対応しています。
その他にも、VPN-over-ICMPと呼ばれるPing通信の上にVPNを構築するもの、VPN-over-DNSと呼ばれるDNS通信の上にVPNを構築できるものなど、強固な通信方式をサポートしています。

## フルリゾルバの構築

これは、8.8.8.8や1.1.1.1などの、自身がキャッシュとなり、世界中のルートサーバー、権威サーバーへDNS問い合わせをするDNSサーバーです。上位サーバーなどが存在せず、本来の名前解決を提供しているサーバーへ問い合わせに行くため、ブロック対象になりません。

## OpenNIC

https://www.opennic.org/

OpenNICは、世界に13種類あるルートサーバーを勝手に増やして、自分たちで新しいトップレベルドメインを運営するプロジェクトです。ルートサーバーや、キャッシュサーバーが存在するため、設定するだけで使用できます。

## Namecoin

Namecoinは、DNS情報をブロックチェーンで管理するプロジェクトです。すでにあるドメインを登録することはできず、新しく「*.bit」ドメインを登録することになります。
P2Pで接続できるため、ブロッキングされた時用にサービス側が取得しておくのがいいかもしれません。

似たようなものに、Torのhidden service（.onionドメインが分散ハッシュテーブルで管理される）やI2Pのドメイン（hostsファイルを手動で共有する）、freenetが存在します。

# 7. 参考文献
https://www.cloudflare.com/ja-jp/