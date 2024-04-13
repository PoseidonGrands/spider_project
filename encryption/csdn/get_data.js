f = function(e) {
            var t = e || null;
            return null == t && (t = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (function(e) {
                var t = 16 * Math.random() | 0;
                return ("x" === e ? t : 3 & t | 8).toString(16)
            }
            ))),
            t
}

var m = function(e) {
            var t = {};
            for (var n in e) {
                var o = n.toLowerCase();
                o.startsWith("x-ca-") && ("x-ca-signature" !== o && "x-ca-signature-headers" !== o && "x-ca-key" !== o && "x-ca-nonce" !== o || (t[o] = e[n]))
            }
            return t
        }
function d(e) {
            for (var t = 1; t < arguments.length; t++) {
                var n = null != arguments[t] ? arguments[t] : {};
                t % 2 ? u(Object(n), !0).forEach((function(t) {
                    p(e, t, n[t])
                }
                )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : u(Object(n)).forEach((function(t) {
                    Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t))
                }
                ))
            }
            return e
        }
h = function(e) {
            var t = e.method
              , n = e.url
              , o = e.appSecret
              , i = e.accept
              , r = e.date
              , s = e.contentType
              , a = e.params
              , l = e.headers
              , c = "";
            a || -1 === n.indexOf("?") ? a || (a = {}) : (a = function(e) {
                var t = {}
                  , n = e.match(/[?&]([^=&#]+)=([^&#]*)/g);
                if (n)
                    for (var o in n) {
                        var i = n[o].split("=")
                          , r = i[0].substr(1)
                          , s = i[1];
                        t[r] ? t[r] = [].concat(t[r], s) : t[r] = s
                    }
                return t
            }(n),
            n = n.split("?")[0]);
            c += "".concat(t, "\n"),
            c += "".concat(i, "\n"),
            c += "".concat("", "\n"),
            c += "".concat(s, "\n"),
            c += "".concat(r, "\n");
            var p, f = m(l), h = d(Array.from(Object.keys(f)).sort());
            try {
                for (h.s(); !(p = h.n()).done; ) {
                    var v = p.value;
                    c += v + ":" + f[v] + "\n"
                }
            } catch (e) {
                h.e(e)
            } finally {
                h.f()
            }
            return c += function(e, t) {
                var n, o = null, i = d(Array.from(Object.keys(t)).sort());
                try {
                    for (i.s(); !(n = i.n()).done; ) {
                        var r = n.value
                          , s = void 0;
                        null !== t[r] && void 0 !== t[r] && (s = "" !== t[r] ? r + "=" + t[r] : r + t[r],
                        o = o ? o + "&" + s : s)
                    }
                } catch (e) {
                    i.e(e)
                } finally {
                    i.f()
                }
                return o ? e + "?" + o : e
            }(n.replace(/^(?=^.{3,255}$)(http(s)?:\/\/)?(www\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.csdn\.net)/, ""), a),
            u.a.HmacSHA256(c, o).toString(u.a.enc.Base64)
        };