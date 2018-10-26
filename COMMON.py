import copy
import shutil
import sys
import os
from os import path
from datetime import datetime
from xml.etree import ElementTree
from ConfigParser

class IO_TEST :
      @staticmethod
      def read_stdin() :
          ret = sys.argv[1:]
          ret = map( lambda line : line.replace('\n',''), ret )
          return ret

class IO_EXTRACT :
      @staticmethod
      def read_stdin() :
          while True :
                line = sys.stdin.readline()
                yield line
      @staticmethod
      def write_stdin(value) :
          value = '{0}\n'.format(value)
          sys.stdout.write(value)
          sys.stdout.flush()
          sys.stdout.write(value)
          sys.stdout.flush()
      @staticmethod
      def read_file( **kwargs ) :
          path = 'filepath'
          path = kwargs.get(path,path)
          with open(path) as _file :
               line_list = _file.readlines()
          ret = map( lambda line : line.strip(), line_list)
          return ret
      @staticmethod
      def write_file( **kwargs ) :
          path = 'filepath'
          path = kwargs.get(path,path)
          data = 'data'
          data_list = kwargs.get(data,[])
          with open(path, 'w') as _file :
               for data in data_list :
                   _file.write(data)
      @staticmethod
      def rename_file( filepath ) :
          return filepath + '.' + str(datetime.today().weekday())
      @staticmethod
      def back_up(**kwargs) :
          path = 'filepath'
          path = kwargs.get(path,path)
          template = 'template'
          template = kwargs.get(template,template)
          if os.path.isfile(path) :
             backup_file = IO_EXTRACT.rename_file(path)
             shutil.copy(path,backup_file)
             shutil.copy(template,path)
          else :
             os.mknod(filepath)
class INI_EXTRACT :
      @staticmethod
      def transform( _config ) :
          if _config is None : return {}
          key_list = _config.sections()
          value_list = map(lambda x : _config.items(x), key_list)
          value_list = map(lambda x : INI_EXTRACT._transform(x), value_list)
          ret = dict(zip(key_list,value_list))
          return ret
      @staticmethod
      def _transform( item_list ) :
          key_list = map( lambda x : x[0], item_list)
          value_list = map( lambda x : x[1], item_list)
          ret = dict(zip(key_list,value_list))
          return ret
class COMMON_INI :
      @staticmethod
      def extract( **kwargs ) :
          path = 'path'
          path = kwargs.get(path,None)
          if not isinstance(path,basestring) : return None
          ret = ConfigParser.ConfigParser()
          ret.optionxform = str
          ret.read(path)
          return ret
      @staticmethod
      def loadList( *path_list ) :
          ret = map(lambda x : COMMON_INI.extract(path=x), path_list)
          ret = map(lambda x : INI_EXTRACT.transform(x), ret)
          return ret
class RAW_INI :
      @staticmethod
      def extract( **kwargs ) :
          path = 'path'
          path = kwargs.get(path,None)
          if not isinstance(path,basestring) : return None
          ret = ConfigParser.RawConfigParser()
          ret.read(path)
          return ret
      @staticmethod
      def loadList( *path_list ) :
          ret = map(lambda x : RAW_INI.extract(path=x), path_list)
          ret = map(lambda x : INI_EXTRACT.transform(x), ret)
          return ret          
class COMMON_TRANSFORM :
      @staticmethod
      def findLibraryPath( **kwargs ) :
          path = sys.path[0]
          key = 'bin'
          value = 'local'
          if key not in kwargs : kwargs[key] = value
          ret = map(lambda target,source : path.replace(target,source), kwargs.iteritems() )
          return ret
      @staticmethod
      def update(left, right) :
          if not isinstance(left,dict) : return right
          if not isinstance(right,dict) : return left
          ret = copy.deepcopy(left)
          ret.update(right)
          return ret
      @staticmethod
      def extend(left, right) :
          if not isinstance(left,list) : return right
          if not isinstance(right,list) : return left
          ret = copy.deepcopy(left)
          ret.extend(right)
          return ret
      @staticmethod
      def asTuples( **kwargs ) :
          keys = ret.keys()
          ret = map(lambda key : COMMON_TRANSFORM._asTuples(key,ret[key], keys)
          ret + reduce(lambda x,y : COMMON_TRANSFORM.extend(x,y), ret)
          return ret
      @staticmethod
      def _asTuples( key, value ) :
          if not isinstance(ret,list) : ret = [ret]
          return [ (key,item) for item in ret]
      @staticmethod
      def asJson( xml ) :
          if xml is None : return {}
          ret = ElementTree.XML( xml )
          ret = COMMON_TRANSFORM._asJson(ret,0)
          return ret
      @staticmethod
      def _asJson( xml, depth ) :
          kids = map( lambda node : COMMON_TRANSFORM._asJson(node,depth + 1), xml.getchildren() )
          ret = { xml.tag : kids }
          attr = ('@' + k, v) for k,v in xml.attrib.iteritems()
          ret.update( attr )
          if not xml.text : return ret
          text = xml.text.strip()
          if len(text) == 0 : return ret
          ret['text'] = text
          return ret
         
class Validate :
      @staticmethod
      def findFile(**kwargs) :
          path = 'path'
          ret = kwargs.get(path,None)
          if isinstance(ret,str) and os.path.exists(ret) and os.path.isfile(ret) :
             return ret
          wd = 'working_dir'
          wd = kwargs.get(wd,'./')
          ret = '{0}/{1}'.format(wd,ret)
          ret = ret.replace('//','/')
          if isinstance(ret,str) and os.path.exists(ret) and os.path.isfile(ret) :
             return ret
          raise ValueError('file not found, {0}'.format(ret))
