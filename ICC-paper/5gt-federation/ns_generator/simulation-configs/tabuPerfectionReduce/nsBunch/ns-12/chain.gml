graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 2
    memory 5
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
    disk 3
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 2
    memory 4
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 3
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
    bw 66
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 155
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 177
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 182
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 62
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 166
  ]
]
