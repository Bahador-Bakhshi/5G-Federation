graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 4
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 15
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 2
    memory 13
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 14
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 138
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 177
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 129
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 60
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 81
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 182
  ]
]
