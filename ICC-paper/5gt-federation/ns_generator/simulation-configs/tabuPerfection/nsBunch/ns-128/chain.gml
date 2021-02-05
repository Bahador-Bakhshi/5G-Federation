graph [
  node [
    id 0
    label 1
    disk 8
    cpu 2
    memory 7
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 2
    memory 14
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 5
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
    disk 4
    cpu 2
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 162
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 163
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 192
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 170
  ]
  edge [
    source 1
    target 5
    delay 26
    bw 157
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 82
  ]
]
