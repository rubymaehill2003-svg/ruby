const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
const S='/tmp/claude-0/-home-user-ruby/b44f2fb9-6eed-5680-a384-23171670d6e5/scratchpad';
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});
const ctx=await b.newContext({viewport:{width:600,height:900},deviceScaleFactor:2});const p=await ctx.newPage();
const only=process.argv[2]?new RegExp(process.argv[2]):null;
for(const f of fs.readdirSync(S+'/render').filter(f=>f.endsWith('.html')).sort()){ if(only&&!only.test(f))continue;
 await p.goto('file://'+S+'/render/'+f,{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(150);
 const el=await p.$('#cap'); await el.screenshot({path:S+'/out/'+f.replace('.html','.jpg'),type:'jpeg',quality:88}); console.log('ok',f);}
await b.close();})();
