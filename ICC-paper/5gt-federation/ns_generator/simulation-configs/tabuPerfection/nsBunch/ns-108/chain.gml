graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 5
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 2
    memory 7
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 7
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 5
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 166
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 173
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 182
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 85
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 200
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 141
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 76
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 66
  ]
]
