graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 15
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 11
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 3
    memory 16
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 197
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 172
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 186
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 162
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 143
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 55
  ]
]
