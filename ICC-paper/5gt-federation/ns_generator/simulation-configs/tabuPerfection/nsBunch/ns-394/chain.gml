graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 14
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 6
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 16
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 5
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 8
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 181
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 152
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 119
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 194
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 156
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 54
  ]
  edge [
    source 3
    target 5
    delay 30
    bw 64
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 66
  ]
]
