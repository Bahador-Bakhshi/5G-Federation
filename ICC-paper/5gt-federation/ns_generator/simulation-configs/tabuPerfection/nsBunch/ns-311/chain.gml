graph [
  node [
    id 0
    label 1
    disk 2
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 4
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 1
    memory 14
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 6
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
    delay 30
    bw 196
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 178
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 72
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 184
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 156
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 151
  ]
]
