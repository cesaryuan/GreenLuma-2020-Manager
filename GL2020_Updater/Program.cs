using System;

namespace GL2020_Updater {
   class Program {
      static void Main(string[] args) {
         var updater = new Updater();
         updater.IsUpdated().Wait();
      }
   }
}
