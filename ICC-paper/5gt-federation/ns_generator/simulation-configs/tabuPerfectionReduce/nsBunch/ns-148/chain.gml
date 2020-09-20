graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 15
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 2
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 9
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 15
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 8
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 176
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 78
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 186
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 157
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 156
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 154
  ]
]
