#
# Collective Knowledge (AI artifact store)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings
form_name='ai_artifact_web_form'
onchange='document.'+form_name+'.submit();'
hextra=''

selector=[
          {'name':'Type', 'key':'type'},
          {'name':'Name', 'key':'name'}
         ]

selector2=[
           {'name':'Compatible Framework', 'key':'compatible_framework'},
           {'name':'OS', 'key':'os'},
           {'name':'Platform', 'key':'platform'},
           {'name':'Pre-built', 'key':'prebuilt'},
           {'name':'CPU', 'key':'cpu'},
           {'name':'GPU_API', 'key':'gpu_api'},
           {'name':'GPU', 'key':'gpu'},
           {'name':'NN', 'key':'nn'},
           {'name':'Compiler (CPU)', 'key':'compiler_cpu'},
           {'name':'Compiler (GPU)', 'key':'compiler_gpu'}
          ]

prune_first_level=100
prune_second_level=50

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# view CK AI artifact store

def dashboard(i):
    """
    Input:  {
              (host)        - Internal web server host
              (port)        - Internal web server port

              (wfe_host)    - External web server host
              (wfe_port)    - External web server port

              (extra_url)   - extra URL
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['action']='start'
    i['module_uoa']='web'
    i['browser']='yes'
    i['template']='ai-artifact'
    i['cid']=''

    return ck.access(i)

##############################################################################
# browse AI artifacts

def browse(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return dashboard(i)

##############################################################################
# show info about AI artifact

def html_viewer(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy
    import time

    # Preparing various parameters to render HTML dashboard
    st=''
    h=''

    bd='<div style="background-color:#bfffbf;margin:5px;">'

    if 'reset_'+form_name in i: reset=True
    else: reset=False

    if 'all_choices_'+form_name in i: all_choices=True
    else: all_choices=False

    bd='<div style="background-color:#bfffbf;margin:5px;">'

    h='<center>\n'
    h+='\n\n<script language="JavaScript">function copyToClipboard (text) {window.prompt ("Copy to clipboard: Ctrl+C, Enter", text);}</script>\n\n' 

    h+=hextra

    # Check host URL prefix and default module/action *********************************************
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':cfg['module_deps']['wfe'],
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']
    url0w=rx['url'] #rx['url_without_template']
    template=rx['template']

    url=url0
    action=i.get('action','')
    muoa=i.get('module_uoa','')

    url+='action=index&module_uoa=wfe&native_action='+action+'&'+'native_module_uoa='+muoa
    url1=url

    # Check if selected
    h+='\n\n'

    cuid=i.get('all_params',{}).get('customization','')
    if cuid=='':
       cuid=i.get('customization','')

    duoa=i.get('data_uoa','')
    muoa=i.get('module_uoa','')

    r=ck.access({'action':'load',
                 'module_uoa':muoa,
                 'data_uoa':duoa})
    if r['return']>0: return r

    path=r['path']
    data=r['dict']
    meta=data.get('meta',{})

    # Check available files
    # Start listing points
    uids=[]
    dirList=os.listdir(path)
    for fn in sorted(dirList):
        if fn.endswith('.meta.json'):
           uid=fn[:-10]
           uids.append(uid)

    # Prepare selector
    onchange='submit()'

    dlm=[]
    for q in uids:
        dlm.append({'name':q, 'value':q})

    ii={'action':'create_selector', 
        'module_uoa':cfg['module_deps']['wfe'],
        'data':dlm, 
        'name':'customization',
        'onchange':onchange}
    if cuid!='' and cuid in uids: ii['selected_value']=cuid
    r=ck.access(ii)
    if r['return']>0: return r
    cuid=r['selected_value']

    h+='Select artifact customization:&nbsp;&nbsp;'+r['html']

    # Load 
    pp=os.path.join(path,cuid+'.meta.json')
    r=ck.load_json_file({'json_file':pp})
    if r['return']==0:
       raw='no'
       cdict=r['dict']

       repo=cdict.get('repo','')
       repo_url=cdict.get('repo_url','')

       if repo!='' and repo_url=='':
          repo_url='https://github.com/ctuning/'+repo

       # Load module desc
       r=ck.access({'action':'load',
                    'module_uoa':cfg['module_deps']['module'],
                    'data_uoa':work['self_module_uid']})
       if r['return']>0: return r
       desc=r['desc'].get('customization_desc',{})

       # Check if notes
       notes=''
       pp=os.path.join(path,cuid+'.html')
       r=ck.load_text_file({'text_file':pp})
       if r['return']==0:
          notes=r['string']

       # Start preparing html
       x='<center><H2>Reusable and customizable AI artifact in the <a href="https://github.com/ctuning/ck/wiki">CK format</a> with JSON API</H2></center>\n'

       x+='<div id="ck_entries_space8"></div>\n'
       x+='<i><center>\n'
       x+='This is an on-going open project - help the community by improving this description <a href="https://github.com/ctuning/ck-ai">here</a>, adding other AI artifacts in the CK format, and joining the growing <a href="http://cknowledge.org/partners.html">CK AI consortium</a>!\n'
       x+='</center></i>\n'
       x+='<div id="ck_entries_space8"></div>\n'

       x+='<H2>Sources:</H2>\n'

       source=meta.get('source','')
       source_ck=meta.get('source_ck','')

       x+='<ul>\n'
       if source!='':
          x+='<li>Source and license: <a href="'+source+'">'+source+'</a>\n</li>'
       if source_ck!='':
          x+='<li>CK repository with this artifact: <a href="'+source_ck+'">'+source_ck+'</a>\n</li>'
       if source_ck!='':
          x+='<li>CK repository with collaborative optimization across diverse platforms/models/datasets/libraries: <a href="http://cKnowledge.org/repo">browse</a>\n</li>'

       x+='</ul>\n'

       if source_ck!='':
          j=source_ck.find('/ctuning/')
          if j>0:
             y=':'+source_ck[j+9:]
          else:
             y=' --repo='+source_ck

          x+='<H2>How to get:</H2>\n'
          x+='<div style="margin-left:20px;font-size:14px;">\n'
          x+='<pre>\n'
          x+='ck pull repo'+y
          x+='</pre>\n'
          x+='</div>\n'

       x+='<H2>Meta description:</H2>\n'

       x+='<div style="margin-left:20px;">\n'
       for k in sorted(cdict):
           sk=str(k)
           if sk==k:
              v=str(cdict[k])

              n=desc.get(k,{}).get('desc','')
              if n=='': n=k

              tp=desc.get(k,{}).get('type','')
              if tp=='url':
                 v='<a href="'+v+'">'+v+'</a>'

              x+='<b>'+n+':</b> '+str(v)+'<br>\n'

       x+='</div\n>'

       if notes=='':
          notes='<i>Not added yet - be the first one to add notes <b><a href="https://github.com/ctuning/ck-ai">here</a></b> !</i>'

       x+='<H2>Installation, usage and optimization notes:</H2>\n'
       x+='<div style="margin-left:20px;font-size:14px;">\n'
       x+=notes
       x+='</div\n>'
       x+='<br>\n'
       x+='<br>\n'

       # Finalize HTML
       h+='<center>\n'
       h+='<div id="ck_box_with_shadow" style="width:98%;">\n'
       h+=x+'\n'
       h+='</div>\n'
       h+='</center>\n'

    else:
       raw='yes'

    return {'return':0, 'raw':raw, 'show_top':'yes', 'html':h, 'style':st}

##############################################################################
# show AI artifacts with universal selector

def show(i):
    """
    Input:  {
               (crowd_module_uoa)       - if rendered from experiment crowdsourcing
               (crowd_key)              - add extra name to Web keys to avoid overlapping with original crowdsourcing HTML
               (crowd_on_change)        - reuse onchange doc from original crowdsourcing HTML

               (highlight_behavior_uid) - highlight specific result (behavior)!
               (highlight_by_user)      - highlight all results from a given user

               (refresh_cache)          - if 'yes', refresh view cache
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy
    import time

    # Preparing various parameters to render HTML dashboard
    h=''
    st=''

    bd='<div style="background-color:#bfffbf;margin:5px;">'

    h+=hextra

    if 'reset_'+form_name in i: reset=True
    else: reset=False

    if 'all_choices_'+form_name in i: all_choices=True
    else: all_choices=False

    # Check host URL prefix and default module/action *********************************************
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':'wfe',
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']
    url0w=rx['url'] #rx['url_without_template']
    template=rx['template']

    url=url0
    action=i.get('action','')
    muoa=i.get('module_uoa','')

    url+='action=index&module_uoa=wfe&native_action='+action+'&'+'native_module_uoa='+muoa
    url1=url

    # Prepare first level of selection with pruning ***********************************************
    r=ck.access({'action':'prepare_selector',
                 'module_uoa':cfg['module_deps']['experiment'],
                 'search_module_uoa':work['self_module_uid'],
                 'original_input':i,
                 'debug': '',
                 'selector':selector,
                 'crowd_key':'',
                 'crowd_on_change':onchange,
                 'url1':url1,
                 'form_name':form_name,
                 'background_div':bd,
                 'skip_html_selector':'yes',
                 'keep_empty':'yes',
                 'add_info':'yes'})
    if r['return']>0: return r

    olst=r['lst'] # original list (if all_choices)
    plst=r['pruned_lst']

    # Sort list ***********************************************************************************
    splst=sorted(plst, key=lambda x: (
        x.get('meta',{}).get('meta',{}).get('type',''), 
        x.get('meta',{}).get('meta',{}).get('name','') 
        ))

    # Prune list **********************************************************************************
    len_plst=len(plst)
    if len_plst>prune_first_level:
       plst=plst[:prune_first_level]

       h+='\n<i>Showing '+str(prune_first_level)+' of '+str(len_plst)+' entries ...</i><br>\n'

    table=[]
    for q in splst:
        path=q['path']
        meta=q['meta']
        meta2=meta.get('meta',{})

        # Read experiment points and cache them or reuse cache (per module)!
        p=os.listdir(path)
        for f in p:
            if f.endswith('.meta.json'):
               r=ck.load_json_file({'json_file':os.path.join(path,f)})
               if r['return']==0:
                  row=r['dict']

                  customize_uid=f[:-10]

                  row['info_data_uoa']=q['data_uoa']
                  row['info_data_uid']=q['data_uid']
                  row['info_data_name']=q['info']['data_name']
                  row['info_path']=q['path']
                  row['info_customize_uid']=customize_uid

                  for k in meta2:
                      row['meta_'+k]=meta2[k]

                  table.append(row)

    # Prepare second level of selection with pruning ***********************************************
    r=ck.access({'action':'prepare_selector',
                 'module_uoa':cfg['module_deps']['experiment'],
                 'search_module_uoa':work['self_module_uid'],
                 'original_input':i,
                 'lst':table,
                 'skip_meta_key':'yes',
                 'debug': '',
                 'selector':selector2,
                 'crowd_key':'',
                 'crowd_on_change':onchange,
                 'url1':url1,
                 'form_name':form_name,
                 'skip_form_init':'yes',
                 'background_div':bd,
                 'keep_empty':'yes'})
    if r['return']>0: return r

    h2=r['html']
    table=r['pruned_lst']

    choices2=r['choices']
    wchoices2=r['wchoices']

    # Prune first list based on second selection*****************************************************************************
    if all_choices:
       nsplst=olst
    elif reset:
       nsplst=splst
    else:
       all_uid=[]
       for row in table:
           duid=row.get('info_data_uid','')
           if duid!='' and duid not in all_uid:
              all_uid.append(duid)

       nsplst=[]
       for q in splst:
           if q['data_uid'] in all_uid:
              nsplst.append(q)

    # Check if too many *****************************************************************************************************
    ltable=len(table)
    min_view=False

    hx=''
    if ltable==0:
        h+='<b>No results found!</b>'
        return {'return':0, 'html':h, 'style':st}

    elif ltable>prune_second_level:
       table=table[:prune_second_level]

       hx='\n<i>Showing '+str(prune_second_level)+' of '+str(ltable)+' AI artifacts ...</i><br>\n'

    # Get unique values and create html selector 1 (after selector 2)
    r=ck.access({'action':'get_unique_keys_from_list',
                 'module_uoa':cfg['module_deps']['experiment'],
                 'lst':nsplst,
                 'selector':selector,
                 'crowd_key':'',
                 'original_input':i})
    if r['return']>0: return 

    choices1=r['choices']
    wchoices1=r['wchoices']

    # Prepare selector 1  (based on choices from selector 2)
    r=ck.access({'action':'prepare_html_selector',
                 'module_uoa':cfg['module_deps']['experiment'],
                 'start_form':'yes',
                 'url1':url1,
                 'form_name':form_name,
                 'background_div':bd,
                 'selector':selector,
                 'crowd_key':'',
                 'crowd_on_change':onchange,
                 'wchoices':wchoices1,
                 'original_input':i,
                 'add_reset':'yes'})
    if r['return']>0: return r
    h1=r['html']

    h+='<center>\n'
    h+='<b>Browse reusable, customizable and unified AI artifacts in the <a href="https://github.com/ctuning/ck-ai">CK format with JSON API</a></b>\n'
    h+='<br>\n'

    h+='<div id="ck_entries_space8"></div>\n'
    h+='<i>\n'
    h+='This is an on-going open project - help the community by adding other AI artifacts in the CK format <a href="https://github.com/ctuning/ck-ai">here</a> and join the growing <a href="http://cknowledge.org/partners.html">CK AI consortium</a>!\n'
    h+='</i><br>\n'
    h+='<div id="ck_entries_space8"></div>\n'

    h+=h1+'\n'+h2

    ltable=len(table)
    min_view=False

    if ltable==0:
        h+='<b>No results found!</b>'
        return {'return':0, 'html':h, 'style':st}

    elif ltable>prune_second_level and view_all!='yes':
       table=table[:prune_second_level]

       h+='\n<i>Showing '+str(prune_second_level)+' of '+str(ltable)+' AI artifacts ...</i><br>\n'

    # Sort again
    stable=sorted(table, key=lambda x: (
        x.get('meta_type',''), 
        x.get('info_data_uoa',''), 
        x.get('meta_name',''), 
        x.get('platform',''),
        x.get('os','')))

    # Get desc 
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['module'],
                 'data_uoa':work['self_module_uid']})
    if r['return']>0: return r
    desc=r['desc'].get('customization_desc',{})

    # Show artifacts
    iq=0
    for t in stable:
        x=''

        iq+=1

        data_uoa=t['info_data_uoa']
        data_uid=t['info_data_uid']
        customize_uid=t['info_customize_uid']

        tp=t.get('meta_type','')
        name=t.get('meta_name','')

        path=t['info_path']

        cid=work['self_module_uid']+':'+data_uid
        self_url=url0w+'wcid='+cid+'&customize='+customize_uid

        # Check if has qr-code cached
        qr=customize_uid+'.cached_qr_code.png'
        p=os.path.join(path, qr)
        if not os.path.isfile(p):
           r=ck.access({'action':'generate',
                        'module_uoa':cfg['module_deps']['qr-code'],
                        'qr_level':6,
                        'image_size':90,
                        'string':self_url,
                        'filename':p})
        if os.path.isfile(p):
           utp=url0+'action=pull&common_func=yes&cid='+cid+'&filename='+qr

           x+='<img src="'+utp+'" align="left"/>\n'
              
        # Prepare full user-friendly name
        fn=t.get('info_data_name','')
        if fn=='' or fn==data_uoa:
           fn=tp+' '+name

        x+=str(iq)+') <b>'+fn+'</b>\n'

        # Sources
        source=t.get('meta_source','')
        source_ck=t.get('meta_source_ck','')

        y=''
        if source!='':
           y='<a href="'+source+'">source & license</a>'
        if source_ck!='':
           if y!='': y+=', '
           y+='<a href="'+source_ck+'">CK repo</a>'
        if y!='':
           x+=' ('+y+')\n'

        x+='<br>\n'

        # Various meta data
        x+='<div id="ck_entries_space4"></div><i><center>\n'
        x+='<div style="padding:5px;">\n'
        y=''
        for k in t:
            if not k.startswith('info_') and not k.startswith('meta_'):
               v=t[k]
               sv=str(v)
               if sv!='':
                  if y!='': y+=', '
                  k1=desc.get(k,{}).get('desc','')
                  if k1=='': k1=k
                  y+=k1+'='+sv

        x+=y
        x+='</div>\n'
        x+='</center></i><div id="ck_entries_space4"></div>\n'
                        
        x+='<div style="text-align:right;">\n'
        x+='[ <a href="'+self_url+'">More info about installation, usage and collaborative optimization</a> ]\n'
        x+='</div>\n'


        h+='<center>\n'
        h+='<div id="ck_box_with_shadow" style="width:98%;min-height:90px;">\n'
        h+=x+'\n'
        h+='</div>\n'
        h+='</center>\n'



    return {'return':0, 'html':h, 'style':st}

##############################################################################
# add AI artifact description

def add(i):
    """
    Input:  {
              (data_uoa)  - AI artifact CK alias (for example, framework-mxnet)
              (data_name) - user-friendly name (for example, Framework MXNet)
              (repo_uoa)  - where to create (by default in ck-ai)

              (type)      - Artifact type
              (name)      - Artifact name

              (source)    - Artifact source URL (original and license)
              (source_ck) - Artifact CK repo URL
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    data_uoa=i.get('data_uoa','')
    if data_uoa=='':
       return {'return':1, 'error':'AI alias is not defined, use "ck add ai-artifact:ALIAS"'}


    # Check if already exists (in such case add notes)
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':data_uoa})
    if r['return']>0 and r['return']!=16: return r

    if r['return']==0:
       path=r['path']
       ck.out('Artifact already exists in '+path)
    else:
       repo_uoa=i.get('repo_uoa','')
       if repo_uoa=='': repo_uoa='ck-ai'

       data_name=i.get('data_name','')
       if data_name=='':
          r=ck.inp({'text':'Enter user-friendly name (for example Framework TensorFlow): '})
          if r['return']>0: return r
          data_name=r['string'].strip()

       tp=i.get('type','')
       if tp=='':
          r=ck.inp({'text':'Enter artifact type (for example dataset): '})
          if r['return']>0: return r
          tp=r['string'].strip().lower()

       name=i.get('name','')
       if name=='':
          r=ck.inp({'text':'Enter artifact name (for example imagenet): '})
          if r['return']>0: return r
          name=r['string'].strip().lower()

       source=i.get('source','')
       if source=='':
          r=ck.inp({'text':'Enter original artifact source URL (or Enter to skip): '})
          if r['return']>0: return r
          source=r['string'].strip()

       source_ck=i.get('source_ck','')
       if source_ck=='':
          r=ck.inp({'text':'Enter related CK repo URL (or Enter to skip): '})
          if r['return']>0: return r
          source_ck=r['string'].strip()

       # Add entry
       r=ck.access({'action':'add',
                    'common_func':'yes',
                    'module_uoa':work['self_module_uid'],
                    'data_uoa':data_uoa,
                    'data_name':data_name,
                    'repo_uoa':repo_uoa,
                    'dict':{'meta':{'type':tp,
                                    'name':name,
                                    'source':source,
                                    'source_ck':source_ck}}})
       if r['return']>0: return r
       path=r['path']

    # Add dummy customization
    ck.out('')
    r=ck.inp({'text':'Add dummy custommization META and HTML to describe how to install, use and optimize this artifact (Y/n): '})
    if r['return']>0: return r
    s=r['string'].strip().lower()

    if s!='n' and s!='no':
       rx=ck.gen_uid({})
       if rx['return']>0: return rx

       customization_uid=rx['data_uid']

       # Get existing description to add dummy
       d={}

       rx=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['module'],
                     'data_uoa':work['self_module_uid']})
       if rx['return']>0: return rx
       desc=rx['desc'].get('customization_desc',{})
       for k in desc:
           d[k]=''

       # Save JSON
       pm=os.path.join(path, customization_uid+'.meta.json')
       rx=ck.save_json_to_file({'json_file':pm, 'dict':d})
       if rx['return']>0: return rx

       # Save HTML
       ph=os.path.join(path, customization_uid+'.html')
       rx=ck.save_text_file({'text_file':ph, 'string':''})
       if rx['return']>0: return rx

       # Print
       ck.out('')
       ck.out('Path to customization JSON: '+pm)
       ck.out('Path to customization HTML: '+ph)

    return r # either from load or add
