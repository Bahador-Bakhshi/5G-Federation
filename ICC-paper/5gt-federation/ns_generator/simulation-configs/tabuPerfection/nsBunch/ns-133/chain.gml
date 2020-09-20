graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 7
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 14
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 3
    memory 16
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 100
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 144
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 143
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 83
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 192
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 156
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 117
  ]
]
