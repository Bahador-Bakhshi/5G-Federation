graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 14
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 7
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 55
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 150
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 104
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 64
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 156
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 148
  ]
]
